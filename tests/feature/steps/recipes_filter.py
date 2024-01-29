from behave import *
from hamcrest import assert_that, is_, equal_to, contains_string

from tests.feature.page_object.home_page import HomePage

from tests.feature.page_object.recipes_page import RecipesPage

use_step_matcher("re")


@given("I am on the Home page")
def step_impl(context):
    context.home_page = HomePage(context.driver, context.wait)
    context.home_page.accept_cookie_banner()


@when('I click "Todas las recetas" on menu bar')
def step_impl(context):
    context.home_page.click_all_recipes_button()
    context.recipes_page = RecipesPage(context.driver, context.wait)


@then("I can see recipes on the page")
def step_impl(context):
    hot_dog_recipe = context.recipes_page.get_hot_dog_recipe()
    assert_that(hot_dog_recipe.is_displayed(), is_(True))


@given("I am on the recipes page")
def step_impl(context):
    # to get from home page to recipes page
    context.home_page = HomePage(context.driver, context.wait)
    context.home_page.accept_cookie_banner()
    context.home_page.click_all_recipes_button()


@when('I click "Tipo de plato" in the recipes filter')
def step_impl(context):
    context.recipes_page.click_course_button()


@step('I click "Postres" in dropdown menu')
def step_impl(context):
    context.recipes_page.click_desserts_button()


@then("I can see desserts recipes")
def step_impl(context):
    total_desserts = context.recipes_page.get_number_desserts_recipes_from_dropdown_menu()
    total_result = context.recipes_page.get_total_result_number_recipes()
    assert_that(total_result, contains_string(total_desserts))


@when('I click "Mostrar más recetas"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When I click "Mostrar más recetas"')


@step("I can see")
def step_impl(context):
