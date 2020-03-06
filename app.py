import streamlit as st

def main():
    st.markdown("# Contagious Coughs & Colds 2019 Commute Calculator")
    st.markdown("""An under-researched, likely invalid, statistical toy to 
                illustrate the power of social separation (and conversely the 
                power of our immune systems) by estimating the 
                probability of encountering someone with a contagious cough or 
                cold during your daily round trip commute into the city.
                This makes no attempt to model transmission vectors, nor
                crowd dynamics, nor self quarantine etc.
                **Do not use this for anything!**""")

    st.markdown("""The probability P(X>0) of a finding at least 1 case in a 
                group of N people given a background number of cases (m) in the 
                local city population (M) is a resample with replacement 
                (m >> 1)""")

    st.latex(r'P(X>0) = 1 - (1-p)^{N} = f, \, \text{ ... where } \, p = \frac{m}{M}')

    commute_people_per_min = {'Walk / Cycle': 1.,
                             'Ferry': 4.,
                            'Train / Subway (direct)': 8., 
                            'Train / Subway (1+ change at a busy station)': 12.}

    commute_method = st.radio('Commute Method', 
                            list(commute_people_per_min.keys()), index=2)
    n_commuters = commute_people_per_min[commute_method]

    st.write(f"""This assumes you come into reasonably close aeresol contact 
                (d < 2m) with an average 
                N = {n_commuters:.0f} new commuters per min over the entire 
                commute, incl. busy stations, crowded streets etc.""")

    commute_duration = st.slider('Commute Duration (mins)', min_value=15, 
    max_value=120, value=45, step=15)

    N = commute_people_per_min[commute_method] * commute_duration * 2
    st.write(f'N = approx {N:.0f} commuters encountered during a round trip commute')

    m = st.slider('Count of live cases (m) in the city', min_value=10, 
                            max_value=5000, value=100, step=50)
    M = st.slider('Population in the city (M)', min_value=500000, 
                            max_value=20000000, value=4000000, step=500000)

    f = 1 - (1-(m/M))**N

    st.write(f"""Est. prob. P(X>0) of encountering a contagious cough or cold during 
             your daily round trip commute is: {f:.1%}""")

    st.write(f"""... and over a 5 day week P(X>0|5 days) = 1 - (1-f)^5 is: 
            {1 - (1-f)**5:.1%}""")



if __name__ == "__main__":
    main()