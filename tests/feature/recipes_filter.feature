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
    And I can see recipes
    When I click "Mostrar más recetas"
    Then I can see more recipes on the page

  Scenario: Eliminate filters
    Given I am on the recipes page
    And I have selected desserts recipes by courses
    And I have selected St Valentine by collection
    When I click remove filter from St Valentine
    Then I can see desserts recipes

  Scenario: Sort recipes
    Given I am on the recipes page
    When I sort recipes by total time
    Then I see recipes sorted by cooking time from low to high





