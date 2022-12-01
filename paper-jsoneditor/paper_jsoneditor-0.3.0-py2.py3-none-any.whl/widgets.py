from django import forms


class JSONWidget(forms.Widget):
    template_name = "paper_jsoneditor/widget.html"
    height = 420

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context["widget"]["height"] = self.height
        return context

    class Media:
        css = {
            "all": [
                "paper_jsoneditor/dist/widget.css"
            ]
        }
        js = [
            "paper_jsoneditor/dist/widget.js",
        ]
