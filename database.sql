create table Registrados
(
    reg_code varchar(30) primary key not null,
    reg_email varchar(200) not null,
    reg_nombre varchar(100) not null
);

create table asistencia
(
    reg_serial serial not null primary key,
    reg_code varchar(30) references Registrados(reg_code),
    reg_date timestamp default current_timestamp
);
