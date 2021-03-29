from flask import url_for
from flask_appbuilder import BaseView, expose, has_access


class MySwaggerView(BaseView):

    route_base = "/swagger_fixed"
    default_view = "ui"
    openapi_uri = "/api/{}/_openapi"

    @expose("/<version>")
    @has_access
    def show(self, version):
        from flask_appbuilder.api.manager import OpenApi
        url = url_for(OpenApi.__name__ + "." + OpenApi.get.__name__, version = version)
        return self.render_template(
            "appbuilder/swagger/swagger.html",
            openapi_uri=url,
        )