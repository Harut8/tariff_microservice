from repository.tariff_db_manager.tariff_db_manager import TariffDbManager
from models.tariff_model.tariff_model import TarifModelForView, InnerModelForTarif, PersonalTarifForCreating
from service.tariff_service_manager.tariff_service_interface import TarifServiceInterface


language_dict = {
            "ru": 0,
            "en": 1,
            "hy": 2
        }


class TariffServiceManager(TarifServiceInterface):

    @staticmethod
    async def get_tarifes_for_view(language)->list[TarifModelForView] | None:
        try:
            temp_ = await TariffDbManager.get_tarifes_for_view()
            lan_ = language_dict[language]
            if temp_ is not None:
                data_for_view = [
                    TarifModelForView(
                        tarif_id=i['tarif_id'],
                        tarif_names=i['tarif_names'][lan_],
                        tarif_month_prices=i['tarif_month_prices'],
                        inner_content=InnerModelForTarif(
                            cassa_names=i['cassa_names'][lan_],
                            cassa_counts=i['cassa_counts'],
                            cassa_prices=i['c_per_price'],
                            manager_names=i['manager_names'][lan_],
                            manager_counts=i['manager_counts'],
                            manager_prices=i['m_per_price'],
                            web_names=i['web_names'][lan_],
                            web_counts=i['web_counts'],
                            web_prices=i['w_m_per_price'],
                            mobile_cassa_names=i['mobile_cassa_names'][lan_],
                            mobile_cassa_counts=i['mobile_cassa_counts'],
                            mobile_prices=i['m_c_per_price'],
                            tarifes_others=i['tarifes_others'], )
                    )
                    for i in temp_
                ]
                return data_for_view
            else:
                return None
        except Exception as e:
            print(e)
            return

    @staticmethod
    async def get_tariff_details(tariff_id):
        try:
            _tariff_details = await TariffDbManager.get_tariff_details(tariff_id)
            if not _tariff_details:
                return None
            return _tariff_details
        except Exception as e:
            print(e)
            return

    @staticmethod
    async def check_summ_and_return(item):
        try:
            summ_ = item.mobile_cass_price * item.mobile_cass_count + \
                    item.cass_stantion_count * item.cass_stantion_price + \
                    item.mobile_cass_count * item.mobile_cass_price + \
                    item.web_manager_price * item.web_manager_count
            return summ_
        except Exception as e:
            print(e)
            return
