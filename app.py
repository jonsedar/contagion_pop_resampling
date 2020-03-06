import streamlit as st

def main():
    st.markdown("# Covid19 Commute Calculator")
    st.markdown("## Should I go to the office today?")
    st.markdown("""A seriously under-researched, likely invalid, statistical toy to 
                illustrate the power of social separation by estimating the 
                probability (f) of encountering a liveCovid19 case on your 
                daily return trip commute into the city.
                This makes no attempt to include the effects of crowd dynamics, 
                nor live cases staying at home, nor transmission vectors.""")

    st.markdown("""Generally, the probability of a finding at least 1 case in a 
                group of N people given a background number of cases in the 
                local city population is a resample with replacement (assume m >> 1)""")

    st.latex(r'P(X>0) = 1 - (1-p)^{N} = f')
    st.latex(r'\text{where:} p = \frac{m}{M} = \frac{\text{count cases in pop}}{\text{count pop}}')

    st.markdown('Assume that N is sampled with replacement from M, assume m >> 1')

    commute_people_per_min = {'Walk / Cycle': 3.,
                             'Ferry': 3.,
                            'Train / Subway (direct)': 8., 
                            'Train / Subway (1+ change)': 20.}

    commute_method = st.radio('Commute Method', list(commute_people_per_min.keys()), index=2)
    n_commuters = commute_people_per_min[commute_method]

    st.write(f'This method assumes you cross paths with an average {n_commuters:.0f} new commuters per minute')

    commute_duration = st.slider('Commute Duration (mins)', min_value=10, max_value=120, value=45, step=15)

    N = commute_people_per_min[commute_method] * commute_duration * 2
    st.write(f'Approx {N:.0f} commuters encountered during a round trip commute')

    m = st.slider('Count of live cases (m) in the city', min_value=10, max_value=5000, value=100, step=50)
    M = st.slider('Population in the city (M)', min_value=500000, max_value=20000000, 
                                                value=4000000, step=500000)

    # # f = st.slider('Probability of encountering a case $f$', min_value=0.01, max_value=0.99, value=0.1, step=0.01)
    # #m = np.round(M * (1 - ((1 - f)**(1/N))))

    f = 1 - (1-(m/M))**N

    st.write("Est. probability (f) of encountering a Covid19 case during your day in the city is:", f'{f:.1%}')

    st.write("Assuming a 5 day week: ", f'{1 - (1-f)**5:.1%}')



if __name__ == "__main__":
    main()