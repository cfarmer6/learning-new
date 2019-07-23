# Project Goals
We want the ability to send a Pub And Sub, along with making a message queue within RabbitMQ. More information below

## How to install RabbitMQ
- Windows (https://www.rabbitmq.com/install-windows.html)
- Linux (https://www.rabbitmq.com/download.html)

## Support Packages for RabbitMQ
- Python (https://pypi.org/project/pika/)
- Node (https://github.com/squaremo/amqp.node)
- C++ (https://github.com/CopernicaMarketingSoftware/AMQP-CPP)

## PubSub RabbitMQ
- For this issue, we want the abilty to have a publisher, 
- It will need a JSON Object (See Down Below What A JSON Object Format).
- We will need a Subscriber that will listen and process the JSON Object and Print It for now

## RabbitMQ Message Queue
- We will want to setup a client (someone sending the message) in JSON Object
- We will want to have a worker listening to that queue and printing out each message it gets
- The Queue will need to be durable along with when a worker comes online it should prefetch whatever the queue may have


### JSON Object

{
    "FIELDKEY": "FIELDVALUE"
}

