from lettuce import step

@step('I should see the following:')
def i_should_see_the_following(step):
	assert step.multiling == """one
two 
three
four 
five"""

