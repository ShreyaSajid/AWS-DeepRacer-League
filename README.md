# AWS-DeepRacer-League
AWS DeepRacer gives you an interesting and fun way to get started with reinforcement learning (RL). RL is an advanced machine learning (ML) technique that takes a very different approach to training models than other machine learning methods. It is about taking suitable actions to maximize rewards in a particular situation. You can learn a lot more about the AWS DeepRacer League [here](https://aws.amazon.com/deepracer/league/).

The following AWS services are involved internally while working with AWS DeepRacer:
- Amazon SageMaker
- AWS RoboMaker 
- Amazon S3
- Amazon Kinesis Video Streams (to stream the simulation video while your car trains and evaluates)
- Amazon CloudWatch (to store and analyze logs and metrics)

## Getting Started
The following links provide a detailed specifications to configure your first car, set the action space, hyperparameters, code your reward function and interpret the reward graph. 
- [AWS Documentation](https://docs.aws.amazon.com/deepracer/latest/developerguide/what-is-deepracer.html)
- [Build Your First AWS DeepRacer Model](https://codingnconcepts.com/aws/aws-deepracer/)
- [AWS DeepRacer: Driven by Reinforcement Learning - Online Course](https://www.aws.training/Details/eLearning?id=32143)

## In this repository...
In this repository, I have included a set of sample reward functions, log analysis notebooks and racing line computations that helped me during my experience at the AWS DeepRacer League '21.

### Reward Function
Reinforcement learning (RL) is an area of machine learning concerned with how an agents should take actions in an environment in order to maximize the notion of cumulative reward. Reward function is a python function where you give higher reward points for good behavior and lower reward points for bad behavior. Different approaches could be used and altered according to the environment and action space specified.

### Log Analysis
We could use a Jupyter notebook to analyze and debug models based on log data generated from the AWS DeepRacer simulation and training environment. With snippets of Python code, you can plot and visualize your model???s training performance through various graphs and heatmaps.

### Optimal Racing Line
Watching hours of motorsport taught me that another way to accelerate your agent's performance would be to train it using an optimal racing path. This could be done by using custom waypoints or coordinates. Here, we calculate a race line around the Monaco track. There are 33 other tracks available, and can be specified according to the requirement. 


