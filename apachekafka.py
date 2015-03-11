func main() {
	config, consumerIdPattern, topic, numConsumers, graphiteConnect, graphiteFlushInterval := resolveConfig()
	startMetrics(graphiteConnect, graphiteFlushInterval)

	ctrlc := make(chan os.Signal, 1)
	signal.Notify(ctrlc, os.Interrupt)

	consumers := make([]*kafkaClient.Consumer, numConsumers)
	for i := 0; i < numConsumers; i++ {
		consumers[i] = startNewConsumer(*config, topic, consumerIdPattern, i)
		time.Sleep(10 * time.Second)
	}

	<-ctrlc
	fmt.Println("Shutdown triggered, closing all alive consumers")
	for _, consumer :=range consumers {
		<-consumer.Close()
	}
	fmt.Println("Successfully shut down all consumers")
}

func startMetrics(graphiteConnect string, graphiteFlushInterval time.Duration) {
	addr, err := net.ResolveTCPAddr('tcp', graphiteConnect)
	if err != nil{
		panic(err)
	}
	go metrics.GraphiteWithConfig(metrics.GraphiteConfig{
		Addr:			addr,
		Registry:		metrics.DefaultRegistry,
		FlushInterval:	graphiteFlushInterval,
		DurationUnit:	time.Second,
		Prefix:			"metrics"
		Precentiles: 	[]float64{0.5, .75, .99, .999}
		})
}

func startNewConsumer(config kafkaClient.ConsumerConfig, topic string, consumerIdPattern string, consumerIndex int) *kafkaClient.Consumer {
	config.Consumerid = fmt.Sprintf(consumerIdPattern, consumerIndex)
	config.Strategy = GetStrategy(config.Consumerid)
	config.WorkerFailureCallback = FailedCallback
	config.WorkerFailureAttemptCallback = FailedAttemptCallback
	consumer := kafkaClient.NewConsumer(&config)
	topics := map[string]int {topic: config.NumConsumerFetchers}
	go func() {
		consumer.StartStatic(topics)
	}()
	return consumer
}

funct GetStrategy(consumerId string) func(*kafkaClient.Worker, *kafkaClient.Message, kafkaClient.TaskId) kafkaClient.WorkerResult{
	consumeRate := metrics.NewRegisteredMeter (fmt.Sprintf("%s-ConsumeRate", consumerId), metrics.DefaultRegistry)
	return func(_*kafkaClient.Worker, msg *kafkaClient.Message, id kafkaClient.TaskId) kafkaClient.WorkerResult{
		kafkaClient.Tracef("main", "Got a message: %s", string(msg.Value))
		consumeRate.Mark(1)

		return kafkaClient.NewSucessfulResult(id)
	}
}

func FailedCallback(wm *kafkaClient.WorkerManager) kafkaClient.FailedDecision {
	kafkaClient.Info ("main", "FailedCallback")

	return kafkaClient.DoNotCommitOffsetAndStop
}

func FailedAttemptCallback(task *kafkaClient.Task, result kafkaClient.WorkerResult) kafkaClient.FailedDecision {
	kafkaClient.Info("main", "Failed attempt")

	return kafkaClient.CommitOffsetAndStop
}


















