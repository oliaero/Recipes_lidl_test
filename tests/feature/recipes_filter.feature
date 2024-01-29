Feature: Recipes filter
  As a user
  I want to put filters in my recipies search
  So I can find faster the recipes that I am interested in

  Scenario: See all recipies
    Given I am on the Home page
    When I click "Todas las recetas" on menu bar
    Then I can see recipes on the page


  Scenario: Filter recipies by course
    Given I am on the recipes page
    When I click "Tipo de plato" in the recipes filter
    And I click "Postres" in dropdown menu
    Then I can see desserts recipes

  Scenario: Load more recipes on the page
    Given I am on the recipes page
    And I can see
      | items   | number |
      | recipes | 36     |
    When I click "Mostrar más recetas"
    Then I can see
      | items   | number |
      | recipes | 72     |


