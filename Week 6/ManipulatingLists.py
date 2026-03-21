class ManipulatingLists:
    @staticmethod
    def main():
        originalMovies = ["a new hope", "empire strikes back", "return of the jedi"]
        copiedMovies = originalMovies.copy()
        copiedMovies[1] = "revenge of the sith"
        originalMovies.sort()
        copiedMovies.reverse()
        for movie in originalMovies:
            print(f"Movie: {movie}, index: {originalMovies.index(movie)}")
        for movie in copiedMovies:
            print(f"Copied Movie: {movie}, index: {copiedMovies.index(movie)}")
ManipulatingLists.main()