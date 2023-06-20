#
# from pydantic_redis import Store, RedisConfig
#
# from models.tariff_model.tariff_model import TarifModelForView
#
#
# class RedisClient:
#     store: Store
#     def __init__(self):
#         # self._connection = redis.Redis(
#         #     host='localhost',
#         #     port=6379)
#         RedisClient.store = Store(
#             name="some_name",
#             redis_config=RedisConfig(db=1, host="localhost", port=6379),
#             redis_config=RedisConfig(db=1, host="localhost", port=6379),
#             life_span_in_seconds=3600,
#         )
#         RedisClient.store.register_model(TarifModelForView)
#         print('REDIS CONNECTED')
#
#     @classmethod
#     def get_pydantic_redis(cls, model):
#         return model.select()
#
#     @classmethod
#     def set_pydantic_var(cls, model):
#         model.insert(model)
#
# RedisClient()
#
# x = TarifModelForView(tarif_id='f3609839-15e2-47b7-bbb9-51e94e1ed13c', tarif_names='ewffr',tarif_month_prices=54 )
# TarifModelForView.insert(x)
# y = TarifModelForView.select()
# print(y)