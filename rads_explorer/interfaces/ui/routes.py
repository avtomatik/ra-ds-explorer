from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader, select_autoescape

from rads_explorer.config.paths import TEMPLATE_DIR
from rads_explorer.container.container import get_container

jinja_env = Environment(
    loader=FileSystemLoader(str(TEMPLATE_DIR)),
    autoescape=select_autoescape(["html", "xml"]),
    cache_size=0,
)


router = APIRouter()


@router.get("/ui", response_class=HTMLResponse)
def home():
    container = get_container()
    certs = container.certificate_service().list_certificates()

    html = """
    <html>
        <head><title>RADS Explorer</title></head>
        <body>
            <h1>Certificates</h1>
            <ul>
    """

    for c in certs.items[:20]:
        html += f"<li>{c.serial_number} - {c.name_attributes.common_name}</li>"

    html += """
            </ul>
        </body>
    </html>
    """

    return html


@router.get("/ui/certificates", response_class=HTMLResponse)
def certificates(request: Request):
    container = get_container()
    certs = container.certificate_service().list_certificates().items

    template = jinja_env.get_template("certificates.html")
    html = template.render(request=request, certs=certs)
    return HTMLResponse(content=html)


@router.get("/ui/reports/expiring", response_class=HTMLResponse)
def expiring(request: Request, days: int = 30):
    container = get_container()
    report = container.report_service().expiring_certificates_report(days)

    template = jinja_env.get_template("report_expiring.html")
    html = template.render(request=request, report=report)
    return HTMLResponse(content=html)
