{
  pkgs }: {
  deps = [
    pkgs.python3
    pkgs.python310Packages.beautifulsoup4
    pkgs.python310Packages.requests
  ];
}