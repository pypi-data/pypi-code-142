depends = ('ITKPyBase', 'ITKRegistrationMethodsv4', 'ITKRegistrationCommon', 'ITKOptimizersv4', 'ITKOptimizers', 'ITKMetricsv4', 'ITKMesh', 'ITKIOMeshBase', 'ITKCommon', )
templates = (  ('ParametersEstimator', 'itk::ParametersEstimator', 'itkParametersEstimatorPD6', True, 'itk::Point< double, 6>, double'),
  ('LandmarkRegistrationEstimator', 'itk::LandmarkRegistrationEstimator', 'itkLandmarkRegistrationEstimatorD6', True, '6'),
  ('RANSAC', 'itk::RANSAC', 'itkRANSACPD6', True, 'itk::Point< double, 6>, double'),
)
factories = ()
