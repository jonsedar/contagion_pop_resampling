import streamlit as st

def main():
    st.markdown("# Covid19 Commute Calculator")
    st.markdown("""An under-researched, likely invalid, statistical toy to 
                illustrate the power of social separation by estimating the 
                probability of encountering a live Covid19 case on your 
                daily return trip commute into the city.
                This makes no attempt to model the effects of crowd dynamics, 
                nor live cases staying at home, nor transmission vectors, etc.
                Do not use this for anything!""")

    st.markdown("""The probability P(X>0) of a finding at least 1 case in a 
                group of N people given a background number of cases (m) in the 
                local city population (M) is a resample with replacement (m >> 1)""")

    st.latex(r'P(X>0) = 1 - (1-p)^{N} = f, \, \text{ ... where } \, p = \frac{m}{M}')

    commute_people_per_min = {'Walk / Cycle': 2.,
                             'Ferry': 3.,
                            'Train / Subway (direct)': 8., 
                            'Train / Subway (1+ change at a busy station)': 12.}

    commute_method = st.radio('Commute Method', list(commute_people_per_min.keys()), index=2)
    n_commuters = commute_people_per_min[commute_method]

    st.write(f"""Using nothing but utter guesswork, this assumes you come 
                into reasonably close contact with an average 
                N = {n_commuters:.0f} new commuters per min over the entire commute, 
                incl. walking through stations, crowded streets etc.""")

    commute_duration = st.slider('Commute Duration (mins)', min_value=10, max_value=120, value=45, step=15)

    N = commute_people_per_min[commute_method] * commute_duration * 2
    st.write(f'N = approx {N:.0f} commuters encountered during a round trip commute')

    m = st.slider('Count of live cases (m) in the city', min_value=10, max_value=5000, value=100, step=50)
    M = st.slider('Population in the city (M)', min_value=500000, max_value=20000000, 
                                                value=4000000, step=500000)

    # # f = st.slider('Probability of encountering a case $f$', min_value=0.01, max_value=0.99, value=0.1, step=0.01)
    # #m = np.round(M * (1 - ((1 - f)**(1/N))))

    f = 1 - (1-(m/M))**N

    st.write(f"""Est. probability P(X>0) of encountering a Covid19 case during 
             your daily return commute is: {f:.1%}""")

    st.write(f"""... and over a 5 day week P(X>0|5 days) = 1 - (1-f)^5 is: 
            {1 - (1-f)**5:.1%}""")



if __name__ == "__main__":
    main()