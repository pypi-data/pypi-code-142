depends = ('ITKPyBase', 'ITKRegistrationCommon', 'ITKCommon', )
templates = (  ('PointFeature', 'itk::PointFeature', 'itkPointFeatureMF3MF3', True, 'itk::PointSet< float,3 >, itk::PointSet< float,3 >'),
  ('PointFeature', 'itk::PointFeature', 'itkPointFeatureMD3MD3', True, 'itk::PointSet< double,3 >, itk::PointSet< double,3 >'),
)
factories = ()
