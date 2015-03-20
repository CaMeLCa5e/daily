func main() {
	config, consumerIdPattern, topic, numConsumers, graphiteConnect, graphiteFlushInterval := resolveConfig()
	startMetrics(graphiteConnect, graphiteFlushInterval)

	ctrlc := make(chan os.Signal, 1)
	signal.Notify(ctrlc, os.Interrupt)

	consumers := make ([]*kafkaClient.Consumer, numConsumers)
	for i := 0; i < numConsumers; i++ {
		consumers[i] = startNewConsumer(*config, topic, consumerIdPattern, i
		time.Sleep(10* time.Second)
	}

	<-ctrlc
	fmt.PrintIn("Shutdown triggered, closing all alive consumers")
	for _, consumer:= range consumers{
		<-consumer.Close()
	}
	fmt.PrintIn("Successfully shut down all consumers")
}

func startMetrics (graphiteConnect string, graphiteFlushInterval time.Duration){
	addr, err := net.ResolveTCPAddr("tcp", graphiteConnect)
	if err != nil{
		panic(err)
	}

func startMetrics(graphiteConnect string, graphiteFlushInterval time.Duration) {
	addr, err := net.ResolveTCPAddr("tcp", graphiteConnect)
	if err != nil {
		panic(err)
	}
	go metrics.GraphiteWithConfig(metrics.GraphiteConfig{
		Addr:  addr,
		FlushInterval: graphiteFlushInterval
		})
}

func GetStrategy(consumerID string) func(*kafkaClient.Worker, )

















