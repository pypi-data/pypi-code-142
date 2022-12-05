import quart

from ..extensions import auth
from ..utils import ViewFuncReturnT


blueprint = quart.Blueprint('powerdns', __name__, template_folder='templates')


@blueprint.route('/', endpoint='index')
async def list_domains() -> ViewFuncReturnT:
    return await quart.render_template('list_domains.html')


@blueprint.route('/domain/<string:domain_name>', endpoint='domain_detail')
async def domain_detail(domain_name: str) -> ViewFuncReturnT:
    current_user = await auth.current_user()

    owns_domain = False
    for domain, _ in current_user.domains:
        if domain == domain_name:
            owns_domain = True
            break

    if not owns_domain:
        return quart.redirect(quart.url_for('index'))

    # TODO: actually fetch the domain data here
