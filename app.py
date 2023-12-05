import streamlit as st
from sqlalchemy import text

list_dokter = ['', 'Dr. Arya', 'Dr. Sari', 'Dr. Jasmine', 'Dr. Fira', 'Dr. Sagara', 'Dr. Sio']
list_jeniskelamin = ['', 'L', 'P']

conn = st.connection("postgresql", type="sql", 
                     url="postgresql://zahra072:gWSib8dZK3Gr@ep-solitary-wildflower-12608316.us-east-2.aws.neon.tech/webapp")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS SCHEDULE (No_Antrian serial,Tanggal_Periksa date, Nama varchar, Jenis_Kelamin char(25), Umur text, Pekerjaan varchar,\
                                                        No_Telp varchar, Alamat varchar, Dokter varchar, Hasil_Diagnosa text);')
    session.execute(query)

st.header('PUSKESMAS DATA MANAGEMENT')
page = st.sidebar.selectbox("Pilih Menu", ["View Data","Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM schedule ORDER By No_Antrian;', ttl="0").set_index('No_Antrian')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO schedule (No_Antrian,Tanggal_Periksa, Nama, Jenis_Kelamin, Umur, Pekerjaan, No_Telp, Alamat, Dokter, Hasil_Diagnosa) \
                          VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1':'', '2':'', '3':'', '4':'[]', '5':'', '6':'', '7':None, '8':None})
            session.commit()

    data = conn.query('SELECT * FROM schedule ORDER By No_Antrian;', ttl="0")
    for _, result in data.iterrows():        
        No_Antrian = result ['No_Antrian'] ,
        Tanggal_Periksa_Lama = result ['Tanggal_Periksa'],
        Nama_Lama = result ['Nama'],
        Jenis_Kelamin_Lama = result ['Jenis_Kelamin'],
        Umur_Lama = result ['Umur'] ,
        Pekerjaan_Lama = result ['Pekerjaan'] ,
        No_Telp_Lama = result ['No_Telp'] ,
        Alamat_Lama = result ['Alamat'],
        Dokter_Lama = result ['Dokter'],
        Hasil_Diagnosa_Lama = result ['Hasil_Diagnosa']
        

        with st.expander(f'a.n. {Nama_Lama}'):
            with st.form(f'data-{No_Antrian}'):
                Tanggal_Periksa_baru = st.date_input("Tanggal_Periksa", Tanggal_Periksa_Lama)
                Nama_baru = st.text_input("Nama", Nama_Lama)
                Jenis_Kelamin_baru = st.selectbox("Jenis_Kelamin", list_Jenis_Kelamin, list_Jenis_Kelamin.index(Jenis_Kelamin_Lama))
                Umur_baru = st.text_input("Umur", Umur_Lama)
                Pekerjaan_baru = st.text_input("Pekerjaan", Pekerjaan_Lama)
                No_Telp_baru = st.text_input("No_Telp", No_Telp_Lama)
                Alamat_baru = st.text_input("Alamat", Alamat_Lama)
                Dokter_baru = st.selectbox("Dokter", list_dokter, list_dokter.index(Dokter_Lama))
                Hasil_Diagnosa_baru = st.text_input ("Hasil_Diagnosa", Hasil_Diagnosa_Lama)

                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE schedule \
                                          SET Tanggal_Pemeriksaan=:1, Nama=:2, Jenis_Kelamin=:3, \
                                          Umur=:4, Pekerjaan=:5, No_Telp=:6, Alamat=:7, Dokter=:8, Hasil_Diagnosa=:9 \
                                          WHERE No_Antrian=:10;')
                            session.execute(query, {'1':Tanggal_Periksa_baru, '2':Nama_baru, '3':str(Jenis_Kelamin_baru), 
                                                    '4':Umur_baru, '5':Pekerjaan_baru, '6':No_Telp_baru, '7':Alamat_baru, '9':str(Dokter_baru), '10':No_Antrian})
                            session.commit()
                            st.experimental_rerun()
                
                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM schedule WHERE No_Antrian=:1;')
                        session.execute(query, {'1':No_Antrian})
                        session.commit()
                        st.experimental_rerun()