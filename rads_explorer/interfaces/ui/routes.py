from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from rads_explorer.container.container import get_container

router = APIRouter()
templates = Jinja2Templates(directory="rads_explorer/interfaces/ui/templates")


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

    return templates.TemplateResponse(
        "certificates.html", {"request": request, "certs": certs}
    )


@router.get("/ui/reports/expiring", response_class=HTMLResponse)
def expiring(request: Request, days: int = 30):
    container = get_container()
    report = container.report_service().expiring_certificates_report(days)

    return templates.TemplateResponse(
        "report_expiring.html", {"request": request, "report": report}
    )
