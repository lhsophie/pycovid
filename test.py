from pycovid import pycovid


pycovid.plot_countries_trend(countries=['Iran', 'Italy', 'Spain', 'Portugal', 'Japan', 'Germany', 'Mexico'],
			casetype=['confirmed'], start_date="2020-01-01", plottype="linear")

pycovid.plot_provinces(country=['China'],  
			casetype=['confirmed'], start_date="2020-2-01", plottype="log")
pycovid.plot_provinces(country=['Australia'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="log")
pycovid.plot_provinces(country=['US'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="linear")
pycovid.plot_provinces(country=['Canada'],  
			casetype=['confirmed'], start_date="2019-12-01", plottype="linear")

pycovid.plot_countries()


