create database igrejasql;
use igrejasql;

create table pessoa(
		codido int not null primary key auto_increment,
	nome varchar(100) not null,
	nomeDaIgreja varchar(100) not null,
	nomeDoPastor varchar(100) not null,
	estadocivil varchar(100) not null,
	telefone varchar(100) not null,
	endereco varchar(100) not null,
	dataDeNascimento date not null,
	dataDeBatismo date not null,
)Engine = InnoDB;

select * from pessoa;

    