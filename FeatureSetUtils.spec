/*
A KBase module: FeatureSetUtils
*/

module FeatureSetUtils {
    /* A boolean - 0 for false, 1 for true.
        @range (0, 1)
    */
    typedef int boolean;

    /* An X/Y/Z style reference
    */
    typedef string obj_ref;

    /*
      required params:
      diff_expression_ref: RNASeqDifferetialExpression object reference
      feature_set_name:  result FeatureSet object name
      p_cutoff: p value cutoff
      q_cutoff: q value cutoff
      fold_scale_type: one of ["linear", "log2+1", "log10+1"]
      fold_change_cutoff: fold change cutoff
      workspace_name: the name of the workspace it gets saved to
    */
    typedef structure{
        obj_ref diff_expression_ref;
        string feature_set_name;
        float p_cutoff;
        float q_cutoff;
        string fold_scale_type;
        float fold_change_cutoff;
        string workspace_name;
    } UploadFeatureSetFromDiffExprInput;

    /*
      result_directory: folder path that holds all files generated by upload_featureset_from_diff_expr
      feature_set_ref: generated FeatureSet object reference
      report_name: report name generated by KBaseReport
      report_ref: report reference generated by KBaseReport
    */
    typedef structure{
        string result_directory;
        obj_ref feature_set_ref;
        string report_name;
        string report_ref;
    }UploadFeatureSetFromDiffExprResult;

    /*  
        upload_featureset_from_diff_expr: create a FeatureSet object from a RNASeqDifferentialExpression object
    */
    funcdef upload_featureset_from_diff_expr(UploadFeatureSetFromDiffExprInput params)
        returns (UploadFeatureSetFromDiffExprResult returnVal) authentication required;
};
