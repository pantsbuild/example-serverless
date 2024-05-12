# Example REST API on AWS

This is a simplified example of a REST API that can be run on AWS using:

 - [API Gateway](https://aws.amazon.com/api-gateway/)
 - [AWS Lambda](https://aws.amazon.com/lambda/)

This example includes the following lambda functions:

    - A Get Item Lambda Function:
        Used solely for retrieving items

    - A Manage Items Lambda Function:
        This lambda handles the rest of the CRUD operations, creating, updating, and deleting items.

Pants allows a lot of flexibility with Lambda Functions. You can use single purpose lambda functions, such as the
get_item function, or a lambda that serves several purposes.

Pants will package both internal and external dependencies across your repo. Keep in mind AWS Lambda [Quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html) for package sizes.



> **_Note:_** This very simplified example uses hard coded examples. We are just storing items in memory. This would likely be a database call in a production app.
