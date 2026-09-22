# SAALF: Semi-Automatic Anomaly Labelling Framework

SAALF is a semi-automatic framework for labelling anomalies in univariate time-series data. Manually labelling anomalies is slow and expert-dependent, and anomalies themselves come in (at least) two different shapes that call for different detection strategies: isolated point-wise outliers, and sustained anomalous regions where the data drifts away from its usual recurring pattern over an extended stretch of time. SAALF combines one component for each:

- **C-WDE** (Confidence-Weighted Detector Ensemble) — runs a small ensemble of anomaly detectors, selected per input series by ADSFra (our earlier data-fingerprinting-based detector-selection framework), and combines their binary signals into point-wise anomaly label candidates using confidence-derived Softmax weights.
- **[SAR](SAR/)** (Sustained Anomaly Recognition) — estimates a periodic "template" pattern (e.g. a daily median profile) from the input series, measures each point's deviation from it, and turns sustained periods of high deviation into anomalous-region label candidates via a merge-then-prune procedure. See [SAR/README.md](SAR/README.md) for how it works and how to run it.

The two components are complementary: C-WDE targets short, structural spikes, while SAR targets extended departures from a series' normal periodic behaviour. Neither component's output is meant to be a final ground-truth label; SAALF is a decision-support tool intended to speed up and guide expert annotation, not replace it.

## Repository structure

```
SAALF/
├── SAR/    # Sustained Anomaly Recognition component - see SAR/README.md
└── ...     # additional components (e.g. C-WDE) may be added here
```

Each component is self-contained (its own `requirements.txt`, its own README) and can be run independently.

## Datasets

None of the datasets used in our experiments are bundled in this repository, since they are third-party benchmarks that aren't ours to redistribute. We evaluated SAALF on:

- **NAB** — the [Numenta Anomaly Benchmark](https://github.com/numenta/NAB).
- **Yahoo Webscope S5** — the A1 ("real") subset ("S5 - A Labeled Anomaly Detection Dataset"). Yahoo's Webscope catalog site (`webscope.sandbox.yahoo.com`) is currently unreachable; request access by emailing `research-data-requests@yahoo-inc.com` with the dataset name, your affiliation, and intended research use (per Yahoo's Webscope Data Sharing Agreement process).
- **IOPS** — a KPI anomaly-detection benchmark, as repackaged by the [TSB-UAD benchmark suite](https://github.com/TheDatumOrg/TSB-UAD) (originally the AIOps 2018 KPI competition data).
- **NEK** (Network Equipment KPI) — a collection of labelled production router/switch KPI series, released alongside TimeSeriesBench; available in the `NEK/` folder of [CSTCloudOps/Dataset-for-TSAD](https://github.com/CSTCloudOps/Dataset-for-TSAD).
- **CESNET-TimeSeries24** — large-scale, mostly unlabelled network telemetry, used to illustrate SAALF's intended use on real, unlabelled data; available on [Zenodo](https://zenodo.org/records/13382427).

See the paper for the exact citations, subsets, and preprocessing used, and [SAR/README.md](SAR/README.md#data) for the folder layout SAR's code expects if you want to reproduce its experiments.

## Citing this work

If you use SAALF in your research, please cite:

> A. R. B. Nayef, D. L. Vajda, K. Farkas. "SAALF -- Semi-Automatic Anomaly Labelling Framework for Time-Series Data."

(Full publication details will be added here once available.)

## License

This project is licensed under the GNU General Public License v3.0 - see [LICENSE](LICENSE) for details.

## Contact

Department of Networked Systems and Services, Faculty of Electrical Engineering and Informatics, Budapest University of Technology and Economics.
