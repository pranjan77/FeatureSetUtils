# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from FeatureSetUtils.Utils.FeatureSetBuilder import FeatureSetBuilder
from FeatureSetUtils.Utils.AveExpressionMatrixBuilder import AveExpressionMatrixBuilder
#END_HEADER


class FeatureSetUtils:
    '''
    Module Name:
    FeatureSetUtils

    Module Description:
    A KBase module: FeatureSetUtils
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.1.1"
    GIT_URL = "https://github.com/Tianhao-Gu/FeatureSetUtils.git"
    GIT_COMMIT_HASH = "a28dad0b99234785cd7cd335d569c1fa804b838d"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def upload_featureset_from_diff_expr(self, ctx, params):
        """
        upload_featureset_from_diff_expr: create a FeatureSet object from a RNASeqDifferentialExpression object
        :param params: instance of type "UploadFeatureSetFromDiffExprInput"
           (required params: diff_expression_ref:
           DifferetialExpressionMatrixSet object reference
           expression_matrix_ref: ExpressionMatrix object reference p_cutoff:
           p value cutoff q_cutoff: q value cutoff fold_scale_type: one of
           ["linear", "log2+1", "log10+1"] fold_change_cutoff: fold change
           cutoff feature_set_suffix: Result FeatureSet object name suffix
           filtered_expression_matrix_suffix: Result ExpressionMatrix object
           name suffix workspace_name: the name of the workspace it gets
           saved to) -> structure: parameter "diff_expression_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter
           "expression_matrix_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "p_cutoff" of Double, parameter "q_cutoff"
           of Double, parameter "fold_scale_type" of String, parameter
           "fold_change_cutoff" of Double, parameter "feature_set_suffix" of
           String, parameter "filtered_expression_matrix_suffix" of String,
           parameter "workspace_name" of String
        :returns: instance of type "UploadFeatureSetFromDiffExprResult"
           (result_directory: folder path that holds all files generated by
           upload_featureset_from_diff_expr up_feature_set_ref: generated
           upper FeatureSet object reference down_feature_set_ref: generated
           down FeatureSet object reference filtered_expression_matrix_ref:
           generated filtered ExpressionMatrix object reference report_name:
           report name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "result_directory" of String, parameter "up_feature_set_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter
           "down_feature_set_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "filtered_expression_matrix_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "report_name" of
           String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN upload_featureset_from_diff_expr
        print '--->\nRunning FeatureSetUtils.upload_featureset_from_diff_expr\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        fs_builder = FeatureSetBuilder(self.config)
        returnVal = fs_builder.upload_featureset_from_diff_expr(params)
        #END upload_featureset_from_diff_expr

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method upload_featureset_from_diff_expr return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def calculate_average_expression_matrix(self, ctx, params):
        """
        calculate_average_expression_matrix: create an average ExpressionMatrix object from a ExpressionMatrix object
        :param params: instance of type "CalAveExpressionMatrixInput"
           (required params: expression_matrix_ref: ExpressionMatrix object
           reference output_suffix: output average ExpressionMatrix name
           suffix workspace_name: the name of the workspace it gets saved to)
           -> structure: parameter "expression_matrix_ref" of type "obj_ref"
           (An X/Y/Z style reference), parameter "output_suffix" of String,
           parameter "workspace_name" of String
        :returns: instance of type "CalAveExpressionMatrixResult"
           (average_expression_matrix_ref: generated average ExpressionMatrix
           object reference report_name: report name generated by KBaseReport
           report_ref: report reference generated by KBaseReport) ->
           structure: parameter "average_expression_matrix_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "report_name" of
           String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN calculate_average_expression_matrix
        print '--->\nRunning FeatureSetUtils.calculate_average_expression_matrix\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        ave_builder = AveExpressionMatrixBuilder(self.config)
        returnVal = ave_builder.calculate_average_expression_matrix(params)
        #END calculate_average_expression_matrix

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method calculate_average_expression_matrix return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
