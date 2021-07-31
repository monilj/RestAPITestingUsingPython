# Created by monil.joshi at 7/31/2021
  # Enter feature name here
Feature: Verify if Books are added and deleted using Library API

  # Enter feature description here
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook PostAPI method
    Then book is successfully added