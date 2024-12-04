def read_data(file_name):
    data = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(';')  
                if len(parts) == 2:
                    name = parts[0].strip()
                    try:
                        score = float(parts[1].strip())
                        data.append((name, score))
                    except ValueError:
                        print(f"Nilai tidak valid pada baris: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_name}' tidak ditemukan.")
        return None
    return data

def calculate_statistics(data):

    total_peserta = len(data)
    rata_rata = sum(score for _, score in data) / total_peserta
    peserta_lulus = [(name, score) for name, score in data if score > 80.0]
    peserta_tertinggi = max(peserta_lulus, key=lambda x: x[1], default=(None, None))
    peserta_terendah = min(data, key=lambda x: x[1], default=(None, None))
    return total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus

def write_results(file_name, total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus):

    with open(file_name, 'w') as file:
        file.write(f'nama file data : {data_file}\n')
        file.write(f'nama file hasil: {result_file}\n')

        file.write(f"Total jumlah peserta: {total_peserta}\n")
        file.write(f"Rata-rata nilai: {rata_rata:.2f}\n")
        if peserta_tertinggi[0]:
            file.write(f"Peserta dengan nilai tertinggi: {peserta_tertinggi[0]} ({peserta_tertinggi[1]:.2f})\n")
        else:
            file.write("Peserta dengan nilai tertinggi: Tidak ada\n")
        if peserta_terendah[0]:
            file.write(f"Peserta dengan nilai terendah: {peserta_terendah[0]} ({peserta_terendah[1]:.2f})\n")
        else:
            file.write("Peserta dengan nilai terendah: Tidak ada\n")
        file.write("=== Daftar peserta LULUS UJI sertifikasi ===\n")
        for name, score in peserta_lulus:
            file.write(f"{name} ({score:.2f})\n")

data_file = 'sertifikasi.txt'.strip()
result_file = "rekap-data.txt".strip()

data = read_data(data_file)
if data:
    total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus = calculate_statistics(data)
    write_results(result_file, total_peserta, rata_rata, peserta_tertinggi, peserta_terendah, peserta_lulus)
    print(f"Hasil telah ditulis ke '{result_file}'.")

with open(result_file, 'r') as file:
        content = file.read()
        print(content)