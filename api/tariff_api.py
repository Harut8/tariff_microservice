from fastapi import APIRouter, Depends, HTTPException, Header
from auth.auth import auth_required
from models.tariff_model.tariff_model import Language, TarifDetails
from service.tariff_service_manager.tariff_service_manager import TariffServiceManager


tariff_router = APIRouter(tags=["TARIFF API"], prefix="/tariff")


@tariff_router.get('/ping')
async def tariff_ping():
    return {"status": "TARIFF PINGING"}


@tariff_router.get("/get-tarifes-for-view/{language}")
@auth_required
async def get_tarifes_for_view(language: Language, authorize=Header(None)):
    _tarifes_for_view = await TariffServiceManager.get_tarifes_for_view(language.value)
    if not _tarifes_for_view:
        return HTTPException(404)
    return _tarifes_for_view


@tariff_router.post("/get-tariff-details")
@auth_required
async def get_tariff_details(tariff_body: TarifDetails, authorize=Header(None)):
    _tariff_details = await TariffServiceManager.get_tariff_details(tariff_body.tarif_id)
    if not _tariff_details:
        return HTTPException(404)
    return _tariff_details

