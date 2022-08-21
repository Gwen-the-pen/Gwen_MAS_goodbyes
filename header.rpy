#https://github.com/Gwen-the-pen

init -990 python in mas_submod_utils:
    Submod(
        author="Gwen",
        name="Gwen's Goodbyes",
        description="New ways to say 'bye' to Monika!",
        version="1.0.0",
        dependencies={},
        settings_pane=None,
        version_updates={
        }
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Gwen's Goodbyes",
            user_name="Gwen-the-pen",
            repository_name="gwens_MAS_goodbyes",
            submod_dir="/Submods",
            extraction_depth=3,
            redirected_files=(
                "README.md",
            )
        )
