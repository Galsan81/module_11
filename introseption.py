

import inspect
import types


def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj)


    info['attributes'] = dir(obj)  # Список всех атрибутов и методов

    # Методы объекта
    if isinstance(obj, types.ModuleType):
        # Если объект является модулем
        info['methods mod'] = dir(obj)
    else:
        # Если это обычный объект (не модуль)
        info['methods obj'] = [func for func in dir(obj) if callable(getattr(obj, func))]

    # Модуль, к которому принадлежит объект
    if  inspect.ismodule(obj) == True:
        info['module'] = obj.__module__
    else:
        info['module'] = 'ne module'
    #info['module'] = inspect.getmodule(obj)
    return info


# Пример использования


number_info = introspection_info(42)
print(number_info)
