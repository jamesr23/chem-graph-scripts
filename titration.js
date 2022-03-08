/* water, nitrate, potassium */
const trials = [
    [33, 4, 4],
    [28, 6, 6],
    [24, 8, 8],
    [20, 10, 10.5],
    [16, 12, 13],
    [12.5, 14, 14],
    [8, 16, 16]
],
    output = [],
    M_ACID = 0.01,
    M_BASE = 0.02;

for (let trial_i = 0; trial_i < trials.length; trial_i++) {
    const trial = trials[trial_i];
    const v_water = trial[0] / 1000,
        v_pb = trial[1] / 1000,
        v_i = trial[2] / 1000;
    const total_volume = (v_water + v_pb + v_i);
    let n_pb = M_ACID * v_pb,
        n_i = M_BASE * v_i;
    let m_pb = n_pb / total_volume,
        m_i = n_i / total_volume;
    let qsp = m_pb * m_i * m_i;
    console.log({
        trial: trial_i + 1, 
        total_volume: `${v_water} + ${v_pb} + ${v_i} = ${total_volume.toFixed(3)}`,
        n_pb: `${M_ACID} * ${v_pb} = ${n_pb.toFixed(5)}`, 
        n_i: `${M_BASE} * ${v_i} = ${n_i.toFixed(5)}`, 
        m_pb: m_pb.toFixed(5), 
        m_i: m_i.toFixed(5), 
        qsp: qsp
    });
}
