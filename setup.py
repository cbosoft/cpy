from distutils.core import setup

def main():
    setup(
        name='cpy',
        description='Simple circuit digraming using pyplot',
        version='0.1',
        packages=['cpy'],
        install_requires=[
            'numpy',
            'matplotlib'
        ]
    )

if __name__ == "__main__":
    main()
