Feature: A call to uploader file

  Scenario: Reporter runs without error
    Given the entrypoint "python"
    And the command "/usr/src/uploader.py"
    And the flags "-e docker"
    When the app is called from the command line
    Then the return code should be 0
