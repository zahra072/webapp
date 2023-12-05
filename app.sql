drop table if exists schedule;
create table schedule (
	No_Antrian serial,
	Tanggal_Periksa date,
	Nama text,
	Jenis_Kelamin text,
	Umur text,
	Pekerjaan text,
	No_Telp text,
	Alamat text,
	Dokter text,
	Hasil_Diagnosa text
);

insert into schedule (No_Antrian,Tanggal_Periksa, Nama, Jenis_Kelamin, Umur, Pekerjaan,	No_Telp, Alamat, Dokter, Hasil_Diagnosa) 
values
	(1, '12-02-2023', 'Rara', 'P', '21', 'Pelajar', '08112152467', 'Jl. Wafello',	'Dr. Arya', 'Otitis media'),
	(2,	'17-02-2023', 'Lisa', 'P', '23', 'Polisi',	'08213678645', 'Jl. Chip Chip', 'Dr. Arya', 'Otitis media'),
	(3, '17-02-2023', 'Wibowo', 'L', '30', 'Guru', '08382781635', 'Jl. Kenangan', 'Dr. Sari', 'tifus'),
	(4, '20-02-2023', 'Arsa', 'L', '18', 'Pelajar', '08112152557', 'Jl. Diponegoro', 'Dr. Jasmine', 'Gigi berlubang'),
	(5, '20-02-2023', 'Nayla', 'P', '19', 'Pelajar', '08233671874', 'Jl. Soetomo', 'Dr. Sari', 'Batuk berdahak'),
	(6, '20-02-2023', 'Mira', 'P', '20', 'Karyawan', '08624572156', 'Jl. Indramayu', 'Dr. Arya', 'Otitis media'),
	(7,	'21-02-2023', 'Wahyu', 'L', '27', 'PNS', '08382787735', 'Jl. A yani', 'Dr. Jasmine' 'Gigi berlubang'),
	(8, '21-02-2023', 'Indra', 'L', '12', 'Pelajar', '08913366321', 'Jl. Tunjungan', 'Dr. Fira', 'DBD'),
	(9, '21-02-2023', 'Miko', 'L', '16', 'Pelajar', '08263256134', 'Jl. Mawar', 'Dr. Sagara', 'flu'),
	(10, '24-02-2023', 'Alya', 'L', '19', 'Pelajar', '08973625122', 'Jl. Melati', 'Dr. Sio', 'alergi')
	;