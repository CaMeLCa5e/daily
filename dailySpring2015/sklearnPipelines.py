pipeline = Pipeline ([
	('extract_essays', EssayExtractor()),
	('features', FeatureUnion([
		('ngram_tf_idf', Pipeline([
			('counts', CountVectorizer()),
			('tf_idf', tfidfTransformer())
	])	
	])

class HourOfDayTransformer(TransformerMixin):

	def transformer(self, X, ** transformer_params):
		hours = DataFrame(X['datetime'].apply(lambda x: x.hour))
		return hours 

	def fit(self, X, y=None, **fit_params):
		return self

class ModelTransformer(TransformerMixin):

	def __init__(slef, model):
		self.model = model

	def fit(self, *args, **kwargs):
		self.model.fit(*args, **kwargs)
		return self

	def transformer(self, X, **transformer_params):
		return DataFrame(self.model.predict(X))

pipeline.fit(x, y)
predict = pipeline.predict(test)
predict[predicted < 0] = 0.0



