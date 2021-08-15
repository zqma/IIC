from setuptools import setup


setup(
    name='IIC',
    version='0.1',
    packages=['proj', 'proj.archs', 'proj.archs.cluster', 'proj.archs.cluster.baselines', 'proj.archs.semisup',
              'proj.archs.segmentation', 'proj.archs.segmentation.baselines', 'proj.utils', 'proj.utils.cluster',
              'proj.utils.cluster.baselines', 'proj.utils.semisup', 'proj.utils.segmentation',
              'proj.utils.segmentation.baselines',
              'proj.datasets', 'proj.datasets.clustering', 'proj.datasets.segmentation',
              'proj.datasets.segmentation.util', 'proj.datasets.segmentation.baselines'],
    url='',
    license='',
    author='Xu Ji',
    author_email='Xu.Ji@Xu.Ji.com',
    description='IIC',
    install_requires=[
        'scikit-learn',
        'tqdm',
        'opencv-python'
    ]
)

"""

'proj.scripts', 'proj.scripts.cluster',
              'proj.scripts.cluster.analysis', 'proj.scripts.cluster.baselines', 'proj.scripts.semisup',
              'proj.scripts.segmentation', 'proj.scripts.segmentation.analysis', 'proj.scripts.segmentation.baselines',
              
              """