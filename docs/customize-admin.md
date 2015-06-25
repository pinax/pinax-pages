# Customize Admin

Customizing the admin functionality can be as complex as overriding the `ModelAdmin`
and `ModelForm` that ships with `pinax-pages` or as simple as just overriding
the `admin/pages/page/change_form.html` template.

Here is an example of an actual customization to use the [ACE Editor](http://ace.c9.io/) for
teaser and body content:


    {% extends "admin/change_form.html" %}
    {% load i18n admin_urls %}
    {% block extrahead %}
        {{ block.super }}
        <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
        <script src="//cdnjs.cloudflare.com/ajax/libs/ace/1.1.8/ace.js"></script>
        <script>
        $(function () {
            var bodyDiv = $("<div>").attr("id", "body-editor"),
                setupEditor = function (editor, textarea) {
                    editor.setTheme("ace/theme/twilight");
                    editor.getSession().setMode("ace/mode/markdown");
                    editor.getSession().setValue(textarea.val());
                    editor.getSession().setUseWrapMode(true);
                    editor.getSession().on('change', function(){
                      textarea.val(editor.getSession().getValue());
                    });
                    editor.getSession().setTabSize(4);
                    editor.getSession().setUseSoftTabs(true);
                };
            $(".field-body div").append(bodyDiv);
            var editor1 = ace.edit("body-editor");
            var textarea1 = $('textarea[name="body"]').hide();
            setupEditor(editor1, textarea1);
        });
        </script>
        <style type="text/css" media="screen">
        #body-editor {
            min-height: 300px;
            width: 80%;
            min-width: 800px;
        }
    </style>
    {% endblock %}