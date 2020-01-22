Feature: common.utils.list_all_filenames

  Background:
    Given the module common.utils


  Scenario: list_all_filenames(...) should flatten lists
    Given the parameters:
      directory: '.'
      regex: '*'
    When I call the list_all_filenames function
    Then the result should contain:
      ./test_all.py
