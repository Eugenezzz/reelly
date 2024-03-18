Feature: Test Scenarios for Subscription & payments page

  Scenario: User can open Subscription & payments page
    Given Open the Main page and verify the "Main menu" header is present
    When Click on Settings option
    And Click on Subscription & payments option
    Then Verify the Subscription page opens
    And Verify title “Subscription & payments” is visible
    And Verify “Upgrade plan” button is available
    And Verify “Back” button is available