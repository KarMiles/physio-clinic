# Automated testing

[Click here for Readme file](/README.md#user-story-testing)

All tests have been placed in folder **tests** in files:
- test_models.py
- test_views.py
- test_forms.py

The following unit tests were run on models, views and forms:

<br>

___
## 1. Testing models

**test_create_post**

Tests that post can be created using Post model.
Checks:
1. test post is an instance of Post model.

**test_create_post_str_representation**

Tests string representation for Post model.
Checks:
1. string representation is equal to post title.

**test_create_comment**

Tests that comment can be created using Comment model.
Checks:
1. test comment is an instance of Comment model.

**test_create_comment_str_representation**

Tests string representation for Comment model.
Checks:
1. test string representation corresponds to 
string representation defined in Comment model.

**test_post_image_defaults_to_placeholder**

Tests that when no image is uploaded image defaults to placeholder.

<br>

___
## 2. Testing views

**test_user_can_login**

Tests that user can login.
Checks:
1. that the client session is in allauth registry.

**test_get_homepage**

Test to check that Home page displays.
Checks:
1. status code is 200 (success)
and correct template is used.

**test_get_post_detail_page**

Test to check that Post Details page displays.
Checks:
1. status code is 200 (success)
and correct template is used.

**test_get_post_edit_page_staff**

Test to check that Edit Post page displays
for authorized user.
Checks:
1. status code is 200 (success)
and correct template is used
for authorized user.

**test_get_post_edit_page_customer**

Test to check that Edit Post page displays
for authorized user.
Checks:
1. status code is 200 (success) and correct template is used for authorized user.

**test_polllist_not_equal_none**

Tests that Poll page loads list of polls.
Checks:
1. that the PollList is not empty.

**test_poll_page**

Test to check that Poll page displays.
Checks:
1. status code is 200 (success)
and correct template is used.

**test_polllist_not_equal_none**

Tests that Poll page loads list of polls.
Checks:
1. that the PollList is not empty.

**test_login_page**

Test to check that Login page displays.
Checks:
1. status code is 200 (success)
2. correct template is used.

**test_contact_page**

Test to check that Contact page displays.
Checks:
1. status code is 200 (success).
2. correct template is used.

**test_booking_page**

Test to check that Booking page displays correctly.
Checks:
1. status code is 200 (success) in case of authorized user.
2. correct template is used
for authorized user.
3. status code is not 200 in case of non-authorized user.

<br>

___
## 3. Testing forms

**test_post_title_is_required**

Tests if the field 'title' is required.
Checks:
1. form is not valid if title is blank.
2. there is an error message when field is empty.
3. default comment shows.

**test_post_title_is_required_filled**

Tests if form with field 'title' containing characters 
is valid.
Checks:
1. form is valid if title contains characters.

**test_excerpt_is_not_required**

Tests that field 'excerpt' is not required.
Checks:
1. form is valid if 'excerpt' field is left blank.

**test_postform_fields_are_explicit_in_form_metaclass**

Tests that only fields in Meta class display in form.
Checks:
1. Fields listed in Meta class.

<br>

___

Automated tests results screenshot:

![Automated testing results](/readme/docs/images/testing/auto_tests_results.jpg)
