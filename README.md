# animal-crossing-api


## Credit for data

Item & villager database was populated using [VillagerDB](https://github.com/jefflomacy/villagerdb) open-source data library.

## TODO

This I need to do still:
- More or less got pagination up and running for "all" routes but possible want to be able to pass in filters.
- Tidy up code as there is a hell of a lot of copy/pasta, too much in fact it makes me a bit sick...
- Probably want to actually create a dev domain as currently dev is using the main route...


## Deploying to Lambda
- Must first set up your AWS this can be done with serverless (google it.)
- Must also have docker open so that it can create a docker build to push up to AWS Lambda.
- Run `serverless deploy --region us-east-2` to push dev build up to AWS Lambda.


