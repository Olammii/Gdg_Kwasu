student = {
        'Abdulsalam' : {
            'Level' : 100,
            'Dept' : 'Computer Science'
            },
        'Abdullah' : {
            'Level' : 200,
            'Dept' : 'PHS'
            },
        'Toheeb': {
            'Level' : 300,
            'Dept' : 'LIS'
            }
        }
for Name, info in student.items():
    print(f"""\nName : {Name}
Level : {info['Level']}
Department : {info['Dept']}
          """)
