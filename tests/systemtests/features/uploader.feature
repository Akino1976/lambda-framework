Feature: A call to uploader file

  Scenario: Reporter runs without error
    Given the bucket bi-framework-data-lake-docker-eu-west-1 is empty
    And the request body:
        event:
          filename: hejhejhej
          some_other_key: nothej
    When I make a POST request to http://lambdaserver/invoke/lambda_function.handle_event
    Then the HTTP status code should be OK
