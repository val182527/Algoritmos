Proceso inicio
	Escribir "insertar parcial1"
	leer parcial1
	Escribir "insertar parcial2"
	leer parcial2
	Escribir "insertar parcial3"
	leer parcial3
	MediaParciales<-(parcial1+parcial2+parcial3)/3
	CParciales<-(55*MediaParciales)/100
	Escribir "Calificacion de parciales: " CParciales
	Escribir "Insertar calificacion examen final"
	leer ExamenF
	CExamenF<-(30*ExamenF)/100
	Escribir "Calificacion del examen final: " CExamenF
	Escribir "Insertar calificacion trabajo final"
	Leer TrabajoF
	CTrabajoF<-(15*TrabajoF)/100
	Escribir "Calificacion del Trabajo final: " CTrabajoF
	CF<-(CParciales+CExamenF+CTrabajoF)
	Escribir "Su calificacion final es: " CF
FinProceso
