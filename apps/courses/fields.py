from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Campo personalizado para manejar el orden de los elementos dentro de un conjunto de campos especificados.


class OrderField(models.PositiveIntegerField):
    # Constructor del campo personalizado. Permite especificar los campos por los cuales se debe ordenar.
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        # Si el valor del campo es None, calcular el valor automáticamente.
        # Esto asegura que los elementos se ordenen correctamente dentro del conjunto de campos especificados.
        if getattr(model_instance, self.attname) is None:
            try:
                # Filtrar el queryset por los campos especificados en for_fields.
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {
                        field: getattr(model_instance, field)
                        for field in self.for_fields
                    }
                    qs = qs.filter(**query)
                # Obtener el último elemento del queryset ordenado por el campo actual.
                try:
                    last_item = qs.latest(self.attname)
                    value = getattr(last_item, self.attname) + 1
                except ObjectDoesNotExist:
                    value = 0

                setattr(model_instance, self.attname, value)

            except ObjectDoesNotExist:
                value = 0

        return super().pre_save(model_instance, add)
