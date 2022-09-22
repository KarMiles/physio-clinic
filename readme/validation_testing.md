# Validation testing

[Click here for Readme file](/README.md#user-story-testing)

## Validators

The following validators were used for testing code correctness:
### W3C Markup Validator 

No errors or warnings were found by [W3C Markup Validator](https://validator.w3.org/)  throughout the site.
<details>
    <summary>Home</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-index.jpg">
</details>
<details>
    <summary>Polls</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-polls.jpg">
</details>
<details>
    <summary>Login</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-login.jpg">
</details>
<details>
    <summary>Contact</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-contact.jpg">
</details>
<details>
    <summary>Booking</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-booking.jpg">
</details>
<details>
    <summary>404</summary>
    <img src="../readme/docs/images/testing/validation/validation-html-404.jpg">
</details>

<br>

### W3C CSS Jigsaw Validator

No errors were found by [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator). Reported warnings are related to Bootstrap and Font Owesome solutions.
<details>
    <summary>CSS Validation</summary>
    <img src="../readme/docs/images/testing/validation/validation-css.jpg">
</details>
<details>
    <summary>Bootstrap</summary>
    <img src="../readme/docs/images/testing/validation/validation-css-bootstrap.jpg">
</details>
<details>
    <summary>Font Owesome</summary>
    <img src="../readme/docs/images/testing/validation/validation-css-fontawesome.jpg">
</details>

<br>

## User Experience UX testing

### Visibility and functionality
Optimal visibility and functionality on various devices was tested throughout the production process and the finished product was tested using [Responsive Designs](http://ami.responsivedesign.is). Screen from this test is placed in the beginning of this document.

<br>

### Accessibility
Testing for accessibility of the site was carried out with the employment of [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/). Initially contrast errors were found. These errors were addressed by increasing contrast on fonts against background and introducing Contrast toggle button in the top left corner. Switching to increased contrast sets font colours outside original colour scheme but enhances reading comfort for users with such visual needs. This functionality works accross all the website. Alerts were addressed where needed.
<details>
    <summary>Home</summary>
    <img src="../readme/docs/images/testing/validation/validation-accessibility-index.jpg">
</details>
<details>
    <summary>Polls</summary>
    <img src="../readme/docs/images/testing/validation/validation-accessibility-polls.jpg">
</details>
<details>
    <summary>Login</summary>
    <img src="../readme/docs/images/testing/validation/validation-accessibility-login.jpg">
</details>
<details>
    <summary>Contact</summary>
    <img src="../readme/docs/images/testing/validation/validation-accessibility-contact.jpg">
</details>
<details>
    <summary>404</summary>
    <img src="../readme/docs/images/testing/validation/validation-accessibility-404.jpg">
</details>

<br>

### Performance
Performance testing was done in [Lighthouse](https://developers.google.com/web/tools/lighthouse), part of the Google Chrome Developer Tools.
 All performance tests ended with score between 90-100.
<details>
    <summary>Home</summary>
    <img src="../readme/docs/images/testing/validation/validation-performance-index.jpg">
</details>
<details>
    <summary>Polls</summary>
    <img src="../readme/docs/images/testing/validation/validation-performance-polls.jpg">
</details>
<details>
    <summary>Login</summary>
    <img src="../readme/docs/images/testing/validation/validation-performance-login.jpg">
</details>
<details>
    <summary>Contact</summary>
    <img src="../readme/docs/images/testing/validation/validation-performance-contact.jpg">
</details>
<details>
    <summary>Booking</summary>
    <img src="../readme/docs/images/testing/validation/validation-performance-booking.jpg">
</details>

<br>

### Python code validation

**Pycodestyle**

Pycodestyle validation tool has been used to identify and remedy errors in Python code with special attention to *unused variables* and *unused imports*.

Setup for pycodestyle validation in contained in [setup.cfg](../setup.cfg) file.

<details>
    <summary>Results</summary>
    <img src="../readme/docs/images/testing/validation/validation-pycodestyle-result.jpg">
</details>

<br>

**Pylint**

Pylint validation tool has been used to identify and remedy errors in Python code with special attention to *missing docstrings*.

Setup for pycodestyle validation in contained in [.pylintrc](../.pylintrc) file.

Ignored positives in this project:

- Unused import env error - has been ingrored as the code works correctly and is necessary for importing from env.py. File: settings.py

    ![Unused import env](../readme/docs/images/testing/validation/validation-pylint-env.jpg)

- Too few public methods - ignored for consistency of the code among its various apps. This way even though the Poll form in CreatePollForm class is simpler than other forms in the project, it still utilizes the same mechanisms as the more complex ones. File: poll/forms.py

- Unused argument 'request' - ignored as most likely a false positive, in that the request needs to be passed to the function, as that's an argument that the function expects, even if it isn't directly accessed. File: booking/views.py 

    ```def post(self, _request):```

- No value for argument 'request' in method call (no-value-for-parameter) - apparently pylint doesn't recognize data in new user form, as code works correctly this message has been disabled. File: accounts/views.py

    <details>
    <summary>Click here to see screenshot</summary>

    ![Unused import env](../readme/docs/images/testing/validation/validation-pylint-request.jpg)
    </details>

- Attribute defined outside init - definition of delete function is derived directly from Django package and expanded by flash message upon success. File: blog/views.py

    <details>
    <summary>Click here to see screenshot</summary>

    ![Unused import env](../readme/docs/images/testing/validation/validation-pylint-delete.jpg)
    </details>

<br>

**PEP8 Online**

For testing Python code PEP8 Online service was used. All tests resulted with "All right" status.

<details>
<summary>accounts/apps.py</summary>

![screenshot](../readme/docs/images/testing/pep8/accounts_apps.jpg)
</details>

<details>
<summary>accounts/forms.py</summary>

![screenshot](../readme/docs/images/testing/pep8/accounts_forms.jpg)
</details>

<details>
<summary>accounts/views.py</summary>

![screenshot](../readme/docs/images/testing/pep8/accounts_views.jpg)
</details>

<details>
<summary>blog/admin.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_admin.jpg)
</details>

<details>
<summary>blog/apps.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_apps.jpg)
</details>

<details>
<summary>blog/forms.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_forms.jpg)
</details>

<details>
<summary>blog/models.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_models.jpg)
</details>

<details>
<summary>blog/urls.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_urls.jpg)
</details>

<details>
<summary>blog/views.py</summary>

![screenshot](../readme/docs/images/testing/pep8/blog_views.jpg)
</details>

<details>
<summary>booking/admin.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_admin.jpg)
</details>

<details>
<summary>booking/apps.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_apps.jpg)
</details>

<details>
<summary>booking/forms.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_forms.jpg)
</details>

<details>
<summary>booking/models.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_models.jpg)
</details>

<details>
<summary>booking/urls.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_urls.jpg)
</details>

<details>
<summary>booking/views.py</summary>

![screenshot](../readme/docs/images/testing/pep8/booking_views.jpg)
</details>

<details>
<summary>contact/admin.py</summary>

![screenshot](../readme/docs/images/testing/pep8/contact_admin.jpg)
</details>

<details>
<summary>contact/apps.py</summary>

![screenshot](../readme/docs/images/testing/pep8/contact_apps.jpg)
</details>

<details>
<summary>contact/forms.py</summary>

![screenshot](../readme/docs/images/testing/pep8/contact_forms.jpg)
</details>

<details>
<summary>contact/models.py</summary>

![screenshot](../readme/docs/images/testing/pep8/contact_models.jpg)
</details>

<details>
<summary>contact/urls.py</summary>

![screenshot](../readme/docs/images/testing/pep8/contact_urls.jpg)
</details>

<details>
<summary>helpers/views.py</summary>

![screenshot](../readme/docs/images/testing/pep8/helpers_views.jpg)
</details>

<details>
<summary>physioproject/urls.py</summary>

![screenshot](../readme/docs/images/testing/pep8/physioproject_urls.jpg)
</details>

<details>
<summary>poll/admin.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_admin.jpg)
</details>

<details>
<summary>poll/apps.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_apps.jpg)
</details>

<details>
<summary>poll/forms.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_forms.jpg)
</details>

<details>
<summary>poll/models.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_models.jpg)
</details>

<details>
<summary>poll/urls.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_urls.jpg)
</details>

<details>
<summary>poll/views.py</summary>

![screenshot](../readme/docs/images/testing/pep8/poll_views.jpg)
</details>
