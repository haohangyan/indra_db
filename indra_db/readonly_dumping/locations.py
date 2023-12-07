import os
from pathlib import Path

TEMP_DIR = os.environ.get("PRINCIPAL_DUMPING_ROOT")
if not TEMP_DIR:
    TEMP_DIR = Path.home().joinpath(".data/indra/db")
else:
    TEMP_DIR = Path(TEMP_DIR)

TEMP_DIR.mkdir(exist_ok=True, parents=True)


__all__ = [
    "TEMP_DIR",
    "PUBMED_MESH_DIR",
    "pubmed_xml_gz_dir",
    "raw_statements_fpath",
    "reading_text_content_fpath",
    "text_refs_fpath",
    "drop_readings_fpath",
    "reading_to_text_ref_map_fpath",
    "processed_stmts_reading_fpath",
    "processed_stmts_fpath",
    "source_counts_reading_fpath",
    "source_counts_knowledgebases_fpath",
    "source_counts_fpath",
    "stmt_hash_to_raw_stmt_ids_fpath",
    "stmt_hash_to_raw_stmt_ids_reading_fpath",
    "stmt_hash_to_raw_stmt_ids_knowledgebases_fpath",
    "raw_id_info_map_fpath",
    "raw_id_info_map_reading_fpath",
    "raw_id_info_map_knowledgebases_fpath",
    "grounded_stmts_fpath",
    "unique_stmts_fpath",
    "refinements_fpath",
    "belief_scores_pkl_fpath",
    "pa_hash_act_type_ag_count_cache",
    "belief_scores_tsv_fpath",
    "reading_ref_link_tsv_fpath",
    "raw_stmt_source_tsv_fpath",
    "PUBMED_MESH_DIR",
    "pubmed_xml_gz_dir",
    "pmid_mesh_map_fpath",
    "pmid_mesh_mti_fpath",
    "pmid_stmt_hash_fpath",
    "pmid_mesh_concept_counts_fpath",
    "pmid_mesh_term_counts_fpath",
    "mk_hash_pmid_sets_fpath",
    "mesh_concept_ref_counts_fpath",
    "mesh_term_ref_counts_fpath",
    "mesh_concepts_meta_fpath",
    "mesh_terms_meta_fpath",
    "raw_stmt_mesh_concepts_fpath",
    "raw_stmt_mesh_terms_fpath",
    "pa_meta_fpath",
    "name_meta_tsv",
    "text_meta_tsv",
    "other_meta_tsv",
    "source_meta_tsv",
    "evidence_counts_tsv",
    "pa_agents_counts_tsv",
]


# Dump files and their derivatives
raw_statements_fpath = TEMP_DIR.joinpath("raw_statements.tsv.gz")
reading_text_content_fpath = TEMP_DIR.joinpath("reading_text_content_meta.tsv.gz")
text_refs_fpath = TEMP_DIR.joinpath("text_refs_principal.tsv.gz")
drop_readings_fpath = TEMP_DIR.joinpath("drop_readings.pkl")
reading_to_text_ref_map_fpath = TEMP_DIR.joinpath("reading_to_text_ref_map.pkl")
processed_stmts_reading_fpath = TEMP_DIR.joinpath("processed_statements_reading.tsv.gz")
processed_stmts_fpath = TEMP_DIR.joinpath("processed_statements.tsv.gz")
source_counts_reading_fpath = TEMP_DIR.joinpath("source_counts_reading.pkl")
source_counts_knowledgebases_fpath = TEMP_DIR.joinpath(
    "source_counts_knowledgebases.pkl"
)
source_counts_fpath = TEMP_DIR.joinpath("source_counts.pkl")
stmt_hash_to_raw_stmt_ids_fpath = TEMP_DIR.joinpath("stmt_hash_to_raw_stmt_ids.pkl")
stmt_hash_to_raw_stmt_ids_reading_fpath = TEMP_DIR.joinpath(
    "stmt_hash_to_raw_stmt_ids_reading.pkl"
)
stmt_hash_to_raw_stmt_ids_knowledgebases_fpath = TEMP_DIR.joinpath(
    "stmt_hash_to_raw_stmt_ids_knowledgebases.pkl"
)
raw_id_info_map_fpath = TEMP_DIR.joinpath("raw_stmt_id_to_info_map.tsv.gz")
raw_id_info_map_reading_fpath = TEMP_DIR.joinpath(
    "raw_stmt_id_to_info_map_reading.tsv.gz"
)
raw_id_info_map_knowledgebases_fpath = TEMP_DIR.joinpath(
    "raw_stmt_id_to_info_map_knowledgebases.tsv.gz"
)
grounded_stmts_fpath = TEMP_DIR.joinpath("grounded_statements.tsv.gz")
unique_stmts_fpath = TEMP_DIR.joinpath("unique_statements.tsv.gz")
refinements_fpath = TEMP_DIR.joinpath("refinements.tsv.gz")
belief_scores_pkl_fpath = TEMP_DIR.joinpath("belief_scores.pkl")
pa_hash_act_type_ag_count_cache = TEMP_DIR.joinpath(
    "pa_hash_act_type_ag_count_cache.pkl")

# Temporary tsv files used for load into readonly db
belief_scores_tsv_fpath = TEMP_DIR.joinpath("belief_scores.tsv")
reading_ref_link_tsv_fpath = TEMP_DIR.joinpath("reading_ref_link.tsv")
raw_stmt_source_tsv_fpath = TEMP_DIR.joinpath("raw_stmt_source.tsv")

# Pubmed XML files
PUBMED_MESH_DIR = TEMP_DIR.joinpath("pubmed_mesh")
pubmed_xml_gz_dir = PUBMED_MESH_DIR.joinpath("pubmed_xml_gz")

# stmt hash-pmid-MeSH map
pmid_mesh_map_fpath = PUBMED_MESH_DIR.joinpath("pmid_mesh_map.pkl")
pmid_mesh_mti_fpath = PUBMED_MESH_DIR.joinpath("pmid_mesh_mti.tsv")
pmid_stmt_hash_fpath = PUBMED_MESH_DIR.joinpath("pmid_stmt_hash.pkl")

# MeshConcept/TermRefCounts
pmid_mesh_concept_counts_fpath = TEMP_DIR.joinpath(
    "pmid_mesh_concept_counts.tsv")
pmid_mesh_term_counts_fpath = TEMP_DIR.joinpath("pmid_mesh_term_counts.tsv")
mk_hash_pmid_sets_fpath = TEMP_DIR.joinpath("mk_hash_pmid_sets.pkl")
mesh_concept_ref_counts_fpath = TEMP_DIR.joinpath(
    "mesh_concept_ref_counts.tsv")
mesh_term_ref_counts_fpath = TEMP_DIR.joinpath("mesh_term_ref_counts.tsv")

# MeshConceptMeta and MeshTermMeta
mesh_concepts_meta_fpath = PUBMED_MESH_DIR.joinpath("mesh_concepts_meta.tsv")
mesh_terms_meta_fpath = PUBMED_MESH_DIR.joinpath("mesh_terms_meta.tsv")

# RawStmtMeshConcepts and RawStmtMeshTerms
raw_stmt_mesh_concepts_fpath = PUBMED_MESH_DIR.joinpath("raw_stmt_mesh_concepts.tsv")
raw_stmt_mesh_terms_fpath = PUBMED_MESH_DIR.joinpath("raw_stmt_mesh_terms.tsv")

# PaMeta and derived files
pa_meta_fpath = TEMP_DIR.joinpath("pa_meta.tsv.gz")
name_meta_tsv = TEMP_DIR.joinpath("name_meta.tsv")
text_meta_tsv = TEMP_DIR.joinpath("text_meta.tsv")
other_meta_tsv = TEMP_DIR.joinpath("other_meta.tsv")

# SourceMeta
source_meta_tsv = TEMP_DIR.joinpath("source_meta.tsv")

# EvidenceCounts
evidence_counts_tsv = TEMP_DIR.joinpath("evidence_counts.tsv")

# PaAgentCounts
pa_agents_counts_tsv = TEMP_DIR.joinpath("pa_agents_counts.tsv")


if __name__ == "__main__":
    # Print the requested path to stdout if there is a match
    import sys
    file_name = sys.argv[1]
    for file_var in __all__:
        if file_var.startswith(file_name):
            if hasattr(sys.modules[__name__], file_var):
                path = getattr(sys.modules[__name__], file_var)
                assert isinstance(path, Path)
                print(path.absolute().as_posix())
                break
    else:
        raise ValueError(f"Could not find file {file_name}")
