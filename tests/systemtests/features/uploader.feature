Feature: A call to uploader file

  Scenario: Reporter runs without error
    Given the bucket bi-framework-data-lake-docker-eu-west-1 is empty
    When I make a POST request to http://lambdaserver/invoke/lambda_function.lambda_handler
    Then the HTTP status code should be OK
