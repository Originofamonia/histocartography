import networkx as nx


# define all the available modules for interpretability 
AVAILABLE_EXPLAINABILITY_METHODS = {
    'pruning_explainer.graph_pruning_explainer': 'GraphPruningExplainer',
    'lrp_explainer.lrp_gnn_explainer': 'LRPGNNExplainer',
    'attention_based_explainer.attention_gnn_explainer': 'AttentionGNNExplainer',
    'saliency_explainer.graph_gradcam_explainer': 'GraphGradCAMExplainer'
}


BASE_S3 = 's3://mlflow/'


# Assuming the class split is the 5-class scenario one 
MODEL_TO_MLFLOW_ID = {
    'cell_graph_model': {
        'attention_based_explainer.attention_gnn_explainer': BASE_S3 + '70a419364cda43548a6e3733ad0ef0b5/artifacts/model_best_val_weighted_f1_score_0',
        'pruning_explainer.graph_pruning_explainer': BASE_S3 + '55ebbd5a765e4a1d80818112212e1875/artifacts/model_best_val_loss_0',
        'lrp_explainer.lrp_gnn_explainer': BASE_S3 + '7ad2792ad69940e0a54dc554af3c4716/artifacts/model_best_val_weighted_f1_score_0',
        'saliency_explainer.graph_gradcam_explainer': BASE_S3 + '7ad2792ad69940e0a54dc554af3c4716/artifacts/model_best_val_weighted_f1_score_0'
    },
    'multi_level_graph_model': {
        'lrp_explainer.lrp_gnn_explainer': BASE_S3 + '5ced95f2b389478cb3e57aaa1c77fc94/artifacts/model_best_val_loss_0'
    }
}


INTERPRETABILITY_MODEL_TYPE_TO_LOAD_FN = {
    'attention_based_explainer.attention_gnn_explainer': 'plain_model_loading',
    'pruning_explainer.graph_pruning_explainer': 'tentative_model_loading',
    'lrp_explainer.lrp_gnn_explainer': 'plain_model_loading',
    'saliency_explainer.graph_gradcam_explainer': 'plain_model_loading'
}


EXPLANATION_TYPE_SAVE_SUBDIR = {
    'attention_based_explainer.attention_gnn_explainer': 'GAT',
    'pruning_explainer.graph_pruning_explainer': 'GNNExplainer',
    'lrp_explainer.lrp_gnn_explainer': 'GraphLRP',
    'saliency_explainer.graph_gradcam_explainer': 'GraphGradCAMExplainer'
}


# define KG encding the class inter-dependencies for 5-class problem 
FIVE_CLASS_NAMES = ['benign', 'pathologicalbenign', 'atypical', 'dcis', 'malignant']
FIVE_CLASS_DEPENDENCY_GRAPH = nx.Graph()
for label in FIVE_CLASS_NAMES:
    FIVE_CLASS_DEPENDENCY_GRAPH.add_node(label)    

FIVE_CLASS_DEPENDENCY_GRAPH.add_edge('benign', 'pathologicalbenign')
FIVE_CLASS_DEPENDENCY_GRAPH.add_edge('pathologicalbenign', 'atypical')
FIVE_CLASS_DEPENDENCY_GRAPH.add_edge('pathologicalbenign', 'dcis')
FIVE_CLASS_DEPENDENCY_GRAPH.add_edge('adh', 'dcis')
FIVE_CLASS_DEPENDENCY_GRAPH.add_edge('dcis', 'malignant')


# define KG encding the class inter-dependencies for 5-class problem 
SEVEN_CLASS_NAMES = ['benign', 'pathologicalbenign', 'udh', 'adh', 'fea', 'dcis', 'malignant']
SEVEN_CLASS_DEPENDENCY_GRAPH = nx.Graph()
for label in FIVE_CLASS_NAMES:
    SEVEN_CLASS_DEPENDENCY_GRAPH.add_node(label)    

SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('benign', 'pathologicalbenign')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('pathologicalbenign', 'udh')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('pathologicalbenign', 'adh')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('pathologicalbenign', 'fea')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('fea', 'dcis')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('udh', 'adh')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('adh', 'dcis')
SEVEN_CLASS_DEPENDENCY_GRAPH.add_edge('dcis', 'malignant')


KEEP_PERCENTAGE_OF_NODE_IMPORTANCE = [1, 0.5, 0.1]
