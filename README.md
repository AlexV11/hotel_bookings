<h1 align="center"> Hotel reservations </h1>

## Índice

* [Descripción](#descripción)
* [Objetivo](#objetivo)
* [Dataset](#dataset)
* [Tecnologías utilizadas](#tecnologías-utilizadas)

## Descripción

El proyecto consiste en predecir si se va a cancelar una reservación en un hotel. Para esto se cuenta con un dataset que contiene información de las reservaciones de un hotel. El dataset cuenta con 19 columnas y 36276 filas. El dataset se encuentra en el archivo `hotel_reservations.csv`.

## Objetivo

El objetivo es predecir si se va a cancelar una reservación en un hotel usando un modelo de clasificación. 

## Dataset

El dataset cuenta con 19 columnas y 36276 filas. El dataset se encuentra en el archivo `hotel_reservations.csv`.

Las columnas son las siguientes:

* 'Booking_ID': Identificador de la reservación 
* 'no_of_adults': Número de adultos 
* 'no_of_children': Número de niños
* 'no_of_weekend_nights': Número de noches de fin de semana
* 'no_of_week_nights': Número de noches de semana
* 'type_of_meal_plan': Tipo de plan de comida 
* 'required_car_parking_space': Espacio de estacionamiento requerido
* 'room_type_reserved': Tipo de habitación reservada
* 'lead_time': Tiempo de anticipación
* 'arrival_year': Año de llegada
* 'arrival_month': Mes de llegada
* 'arrival_date': Día de llegada
* 'market_segment_type': Tipo de segmento de mercado
* 'repeat_guest': Si es un huésped repetido
* 'no_of_previous_cancellations': Número de cancelaciones anteriores
* 'no_of_previous_bookings_not_canceled': Número de reservaciones anteriores no canceladas
* 'avg_price_per_room': Precio promedio por habitación
* 'no_of_special_requests': Número de solicitudes especiales
* 'booking_status': Estado de la reservación

## Tecnologías utilizadas

* Python